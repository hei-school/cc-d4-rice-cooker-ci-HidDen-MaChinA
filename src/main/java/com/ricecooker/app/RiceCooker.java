package com.ricecooker.app;

import java.util.ArrayList;
import java.util.List;

public class RiceCooker {
    private boolean isPluggedIn = false;
    private boolean isFilled = false;
    private boolean isBroken = false;
    private List<String> content;

    public RiceCooker() {
        content = new ArrayList<String>();
    }

    public RiceCooker setContent(List<String> value) {
        if (!(value instanceof ArrayList)) {
            throw new IllegalArgumentException("dude...you need an array");
        }
        if (value.size() > 20) {
            throw new IllegalArgumentException("you can't have more than 20 food inside it");
        }
        content = value;
        return this;
    }

    public String plugInOrOutThatRiceCooker() {
        if (isBroken) {
            return "my guy...you thrown it into a person...it's broken";
        }
        isPluggedIn = !isPluggedIn;
        return isPluggedIn ? "oke now it's plugged in" : "now we removed the plug";
    }

    public String addInSomeFoodToCook(String food) {
        if (!isFilled) {
            content.add(food);
            if (content.size() == 20) {
                isFilled = true;
            }
            return "added a food : " + food;
        }
        return "oke bro...I don't know what you are cooking but I don't think it's comestible";
    }

    public String listEachFoodInside() {
        if (content.isEmpty()) {
            return "no food inside this";
        }
        StringBuilder toReturn = new StringBuilder("each food inside the rice-cooker, even if you shouldn't have more than rice in it");
        for (String value : content) {
            toReturn.append("\n").append(value);
        }
        return toReturn.toString();
    }

    public String getTheDish(String dishName) {
        content.clear();
        return "oke here is your dish: " + dishName + "\nanyway I think all you should do with a rice-cooker is...cook rice, if you wanted to cook some steak or something like that inside of it, the only place you belong is in jail.";
    }

    public String throwAtPeople() {
        isBroken = true;
        return "oke...you're dumb...or you are just...dumb...oke...anyway the rice-cooker is broken";
    }
}