package com.ricecooker.app.utils;

import com.ricecooker.app.RiceCooker;

import java.util.ArrayList;
import java.util.List;

public class RiceCookerUtil {
    public RiceCookerUtil(){

    }
    public RiceCooker getCooker(List<String> content){
        return new RiceCooker().setContent(content == null ? new ArrayList<String>() : content);
    }
}
