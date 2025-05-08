public class Solution {
    public String solution(String m, String[] musicinfos) {
        String targetMelody = normalizeMelody(m);
        
        String answer = "(None)";
        int maxPlayTime = -1;
        
        for (String musicInfo : musicinfos) {
            String[] parts = musicInfo.split(",");
            String start = parts[0];
            String end = parts[1];
            String title = parts[2];
            String sheetMelody = normalizeMelody(parts[3]);
            
            int playTime = calculateMinutes(start, end);
            
            String playedMelody = buildPlayedMelody(sheetMelody, playTime);
            
            if (playedMelody.contains(targetMelody) && playTime > maxPlayTime) {
                maxPlayTime = playTime;
                answer = title;
            }
        }
        
        return answer;
    }
    
    private int calculateMinutes(String startTime, String endTime) {
        String[] s = startTime.split(":");
        String[] e = endTime.split(":");
        int startH = Integer.parseInt(s[0]);
        int startM = Integer.parseInt(s[1]);
        int endH = Integer.parseInt(e[0]);
        int endM = Integer.parseInt(e[1]);
        
        return (endH*60+endM) - (startH*60+startM);
    }
    
    private String buildPlayedMelody(String sheetMelody, int playTime) {
        StringBuilder played = new StringBuilder();
        int sheetLen = sheetMelody.length();
        
        int fullRepeats = playTime / sheetLen;
        for (int i = 0; i < fullRepeats; i++) {
            played.append(sheetMelody);
        }
        
        int remain = playTime % sheetMelody.length();
        String part = sheetMelody.substring(0, remain);
        played.append(part);

        return played.toString();
    }
    
    private String normalizeMelody(String melody) {
        return melody
            .replace("C#", "1")
            .replace("D#", "2")
            .replace("F#", "3")
            .replace("G#", "4")
            .replace("A#", "5")
            .replace("B#", "6");
    }
}