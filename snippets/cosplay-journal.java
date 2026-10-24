public class Participation {
    // …
    public void addParticipant(Participant participant) {
        if (participant == null) {
            throw new InvalidParticipationDataException("El participante a añadir no puede ser nulo");
        }

        boolean alreadyExists = participants.stream()
                .anyMatch(p -> p.getUserId().equalsIgnoreCase(participant.getUserId()));

        if (alreadyExists) {
            throw new InvalidParticipationDataException("El usuario '" + participant.getUserId() + "' ya forma parte de esta participación");
        }

        if (type == ParticipationType.INDIVIDUAL && participants.size() >= 1) {
            throw new InvalidParticipationDataException("Una participación individual no puede tener más de 1 participante");
        }
        if (type == ParticipationType.DUO && participants.size() >= 2) {
            throw new InvalidParticipationDataException("Una participación en dúo no puede tener más de 2 participantes");
        }

        this.participants.add(participant);
        this.updatedAt = Instant.now();
    }

    public void changeStatus(ParticipationStatus newStatus) {
        if (newStatus == null) {
            throw new InvalidParticipationDataException("El estado de la participación no puede ser nulo");
        }

        if (newStatus == ParticipationStatus.CONFIRMED || newStatus == ParticipationStatus.FINISHED) {
            validateParticipantCountForStatus();
        }

        this.status = newStatus;
        this.updatedAt = Instant.now();
    }

    private void validateParticipantCountForStatus() {
        int count = participants.size();
        if (type == ParticipationType.INDIVIDUAL && count != 1) {
            throw new InvalidParticipationDataException("Una participación individual confirmada debe tener exactamente 1 participante (actual: " + count + ")");
        }
        if (type == ParticipationType.DUO && count != 2) {
            throw new InvalidParticipationDataException("Una participación en dúo confirmada debe tener exactamente 2 participantes (actual: " + count + ")");
        }
        if (type == ParticipationType.GROUP && count < 3) {
            throw new InvalidParticipationDataException("Una participación grupal confirmada debe tener al menos 3 participantes (actual: " + count + ")");
        }
    }
}
