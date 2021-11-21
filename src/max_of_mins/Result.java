package max_of_mins;

import java.util.ArrayDeque;
import java.util.Deque;

public class Result {
    
    /**
     * https://www.hackerrank.com/challenges/min-max-riddle/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
     */
    static long[] riddle(long[] arr) {
        long[] maxes = new long[arr.length];
        for (int windowSize = 1; windowSize <= arr.length; windowSize++) {
            Deque<Long> deque = new ArrayDeque<>();
            long[] windowMins = new long[arr.length - windowSize + 1];
            for (int i = 0; i < arr.length; i++) {
                deque.addFirst(arr[i]);
                if (deque.size() > windowSize) {
                    deque.pollLast();
                }
                if (deque.size() == windowSize) {
                    windowMins[i - windowSize + 1] = min(deque);
                }
            }
            maxes[windowSize - 1] = max(windowMins);
        }

        return maxes;
    }

    private static long min(Deque<Long> queue) {
        long min = Long.MAX_VALUE;
        for(Long v:queue) {
            if (v < min) min = v;
        }
        return min;
    }

    private static long max(long[] arr) {
        long max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) max = arr[i];
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println(Result.riddle(new long[]{2, 6, 1, 12}));
    }

}
