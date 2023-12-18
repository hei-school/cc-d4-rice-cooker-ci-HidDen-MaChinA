using System;
using RiceCookerProject;

namespace RiceCookerProject.Tests
{
    [TestClass]
    public class RiceCookerTests
    {
        [TestMethod]
        public void PlugInOrOutThatRiceCooker_PlugIn_Success()
        {
            // Arrange
            RiceCooker riceCooker = new RiceCooker(5);

            // Act
            string result = riceCooker.PlugInOrOutThatRiceCooker();

            // Assert
            Assert.AreEqual("oke now it's plugged in", result);
            Assert.IsTrue(riceCooker.IsPluggedIn);
        }

        [TestMethod]
        public void AddInSomeFoodToCook_LessThanLimit_Success()
        {
            // Arrange
            RiceCooker riceCooker = new RiceCooker(5);

            // Act
            string result = riceCooker.AddInSomeFoodToCook("Rice");

            // Assert
            Assert.AreEqual("your food was added inside bro", result);
            CollectionAssert.Contains(riceCooker.content, "Rice");
        }

        [TestMethod]
        public void ListAllTheFoodInside_NoFood_Success()
        {
            // Arrange
            RiceCooker riceCooker = new RiceCooker(5);

            // Act
            string result = riceCooker.ListAllTheFoodInside();

            // Assert
            Assert.AreEqual("the food inside the rice cooker are:", result);
        }

        [TestMethod]
        public void GetTheDish_FoodPresent_Success()
        {
            // Arrange
            RiceCooker riceCooker = new RiceCooker(5);
            riceCooker.AddInSomeFoodToCook("Rice");
            riceCooker.AddInSomeFoodToCook("Vegetables");

            // Act
            string result = riceCooker.GetTheDish("Fried Rice");

            // Assert
            Assert.AreEqual("your dish: Fried Rice, was composed of:\nRice\nVegetables", result);
            Assert.AreEqual(0, riceCooker.content.Count);
        }

        [TestMethod]
        public void ThrowAtPeople_RiceCookerBroken_Success()
        {
            // Arrange
            RiceCooker riceCooker = new RiceCooker(5);

            // Act
            string result = riceCooker.ThrowAtPeople();

            // Assert
            Assert.AreEqual("you throw it to people and you pride with it", result);
            Assert.IsTrue(riceCooker.IsBroken);
        }

        [TestMethod]
        [ExpectedException(typeof(Exception), "your limit food inside the rice cooker must be between 0 and 10")]
        public void Constructor_InvalidLimit_ThrowsException()
        {
            // Act & Assert
            RiceCooker riceCooker = new RiceCooker(15);
        }
    }
}