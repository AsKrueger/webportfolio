public final class CostCalculator {

    private static final int INTERNAL_SCALE = 8;
    private static final int FINAL_SCALE = 4;
    private static final BigDecimal HUNDRED = new BigDecimal("100");
    private static final BigDecimal THOUSAND = new BigDecimal("1000");
    // …
    public static CostCalculationResult calculate(
            CostCalculationInput input,
            LocalDateTime calculationDateTime,
            BigDecimal marginPercentage,
            BigDecimal safetyPercentage,
            ElectricityPriceProvider priceProvider) {

        validateInputs(input, calculationDateTime, marginPercentage, safetyPercentage, priceProvider);

        BigDecimal materialCost = calculateMaterialCost(input);
        BigDecimal machineCost = calculateMachineCost(input);
        BigDecimal toolCost = calculateToolCost(input);
        BigDecimal laborCost = calculateLaborCost(input);
        BigDecimal electricityCost = calculateElectricityCost(input, calculationDateTime, priceProvider);

        BigDecimal baseCost = materialCost
                .add(machineCost)
                .add(toolCost)
                .add(laborCost)
                .add(electricityCost);

        BigDecimal safetyAmount = baseCost.multiply(safetyPercentage)
                .divide(HUNDRED, INTERNAL_SCALE, RoundingMode.HALF_UP);

        BigDecimal adjustedCost = baseCost.add(safetyAmount);

        BigDecimal profitAmount = adjustedCost.multiply(marginPercentage)
                .divide(HUNDRED, INTERNAL_SCALE, RoundingMode.HALF_UP);

        BigDecimal finalPrice = adjustedCost.add(profitAmount);

        return new CostCalculationResult(
                scaleToFinal(materialCost),
                scaleToFinal(machineCost),
                scaleToFinal(toolCost),
                scaleToFinal(laborCost),
                scaleToFinal(electricityCost),
                scaleToFinal(baseCost),
                scaleToFinal(safetyAmount),
                scaleToFinal(adjustedCost),
                scaleToFinal(profitAmount),
                scaleToFinal(finalPrice)
        );
    }
    // …
}
