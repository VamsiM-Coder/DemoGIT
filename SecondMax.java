class SecondMax {
    public static void main(String args[]) {
        int horseScores[] = {7,3,5,8,10,11,13,12};

        int n = horseScores.length;

        int firstMaxScore = horseScores[0];
        int secondMaxScore = horseScores[0];

        for(int i = 1; i < n; i++) {
            if(horseScores[i] > firstMaxScore) {
                secondMaxScore = firstMaxScore;
                firstMaxScore = horseScores[i];
            }
            else if(horseScores[i] < firstMaxScore && horseScores[i] > secondMaxScore) {
                secondMaxScore = horseScores[i];
            }
        }

        System.out.println("Second Maximum is: " + secondMaxScore);
    }
}