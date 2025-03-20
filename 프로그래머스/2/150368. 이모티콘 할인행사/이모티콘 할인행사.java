import java.util.*;

class Solution {
    static int[] discountRates = {10, 20, 30, 40};
    static int maxSubscribers, maxRevenue, minDiscountIndex;

    public int[] solution(int[][] users, int[] emoticons) {
        maxSubscribers = 0;
        maxRevenue = 0;
        minDiscountIndex = getMinDiscountIndex(users);

        int[] selectedDiscounts = new int[emoticons.length];
        findBestDiscountCombination(selectedDiscounts, 0, users, emoticons);

        return new int[]{maxSubscribers, maxRevenue};
    }

    private int getMinDiscountIndex(int[][] users) {
        int minDiscount = Integer.MAX_VALUE;
        for (int[] user : users) {
            minDiscount = Math.min(minDiscount, user[0]);
        }
        for (int i = 0; i < discountRates.length; i++) {
            if (minDiscount <= discountRates[i]) {
                return i;
            }
        }
        return 0;
    }

    private void findBestDiscountCombination(int[] selectedDiscounts, int index, int[][] users, int[] emoticons) {
        if (index == emoticons.length) {
            calculateRevenueAndSubscribers(users, emoticons, selectedDiscounts);
            return;
        }

        for (int i = minDiscountIndex; i < discountRates.length; i++) {
            selectedDiscounts[index] = discountRates[i];
            findBestDiscountCombination(selectedDiscounts, index + 1, users, emoticons);
        }
    }

    private void calculateRevenueAndSubscribers(int[][] users, int[] emoticons, int[] discounts) {
        int subscriberCount = 0;
        int revenue = 0;

        for (int[] user : users) {
            int requiredDiscount = user[0];
            int maxBudget = user[1];
            int totalSpent = 0;

            for (int i = 0; i < discounts.length; i++) {
                if (discounts[i] >= requiredDiscount) {
                    totalSpent += getDiscountedPrice(emoticons[i], discounts[i]);
                }
            }

            if (totalSpent >= maxBudget) {
                subscriberCount++;
            } else {
                revenue += totalSpent;
            }
        }

        if (subscriberCount > maxSubscribers || 
            (subscriberCount == maxSubscribers && revenue > maxRevenue)) {
            maxSubscribers = subscriberCount;
            maxRevenue = revenue;
        }
    }

    private int getDiscountedPrice(int price, int discount) {
        return price * (100 - discount) / 100;
    }
}
