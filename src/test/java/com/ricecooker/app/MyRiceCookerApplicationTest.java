package com.ricecooker.app;

import com.ricecooker.app.utils.RiceCookerUtil;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MyRiceCookerApplicationTest {
	private RiceCookerUtil util = new RiceCookerUtil();
	public MyRiceCookerApplicationTest(){

	}
	@Test
	public void plugInRiceCooker() {
		assertEquals(util.getCooker(null).plugInOrOutThatRiceCooker(),"oke now it's plugged in");
	}
	@Test
	public void ThrowAtPeople(){
		assertEquals(util.getCooker(null).throwAtPeople(),"oke...you're dumb...or you are just...dumb...oke...anyway the rice-cooker is broken");
	}
	@Test
	public void plugInRiceCookerButItIsBroken() {
		RiceCooker testing = util.getCooker(null);
		testing.throwAtPeople();
		assertEquals(testing.plugInOrOutThatRiceCooker(),"my guy...you thrown it into a person...it's broken");
	}
	@Test
	public void addingInSomeFood() {
		assertEquals(util.getCooker(null).addInSomeFoodToCook("voanjo"), "added a food : voanjo");
	}
	@Test
	public void listAllTheFoodInsideTheRiceCooker() {
		RiceCooker testing = util.getCooker(null);
		testing.addInSomeFoodToCook("rice");
		testing.addInSomeFoodToCook("sakay");
		assertEquals(testing.listEachFoodInside(), "each food inside the rice-cooker, even if you shouldn't have more than rice in it\nrice\nsakay");
	}
	@Test
	public void returnNotFoodWhenYouListEmptyRiceCookerContent() {
		assertEquals(util.getCooker(null).listEachFoodInside(), "no food inside this");
	}
}
