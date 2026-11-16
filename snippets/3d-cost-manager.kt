/**
 * Precio con IVA (lo que paga el cliente) tal que, tras quitar el IVA y la comisión del canal,
 * queda el coste más el beneficio buscado:
 *   bruto / (1 + iva) - bruto * comisión - fijo = coste + beneficio
 * La comisión de los marketplaces se cobra sobre el total que paga el cliente.
 */
private fun price(
    cost: BigDecimal,
    pricing: Pricing,
    channel: ChannelFees,
    vatPercent: BigDecimal,
    rounding: PriceRounding
): Priced {
    val vat = vatPercent.nonNeg().div(HUNDRED)
    val fee = channel.feePercent.nonNeg().div(HUNDRED)
    val fixed = channel.fixedFee.nonNeg()
    val netFactor = BigDecimal.ONE.div(BigDecimal.ONE + vat) - fee

    val gross: BigDecimal
    var feasible = true
    when (pricing.mode) {
        PricingMode.FIXED_PRICE -> gross = pricing.value.nonNeg()
        PricingMode.MARKUP, PricingMode.TARGET_PROFIT -> {
            val target = if (pricing.mode == PricingMode.MARKUP)
                cost * pricing.value.nonNeg().div(HUNDRED) else pricing.value.nonNeg()
            if (netFactor.signum() <= 0) {
                // Comisión e IVA se comen todo el precio: no hay precio que dé beneficio
                feasible = false
                gross = zero()
            } else {
                gross = rounding.roundUp((cost + target + fixed).div(netFactor))
            }
        }
    }

    val vatAmount = gross - gross.div(BigDecimal.ONE + vat)
    val fees = if (gross.signum() == 0) zero() else gross * fee + fixed
    val profit = gross - vatAmount - fees - cost
    return Priced(gross, vatAmount, fees, profit, feasible)
}
