namespace RiceCookerProject
{
    public class RiceCooker
    {
        public bool IsPluggedIn { get; set; }
        public bool IsFilled { get; set; }
        public bool IsBroken { get; set; }
        public int Limit { get; set; }
        public List<string> content = new List<string>();
        public RiceCooker(int limit)
        {
            if (limit < 0 | limit > 10)
            {
                throw new Exception("your limit food inside the rice cooker must be between 0 and 10");
            }
            Limit = limit;
        }
        public string PlugInOrOutThatRiceCooker()
        {
            if (IsBroken)
            {
                return "You thrown it into a person so it broke";
            }
            IsPluggedIn = !IsPluggedIn;
            return IsPluggedIn ? "oke now it's plugged in" : "now you removed the plug";
        }
        public string AddInSomeFoodToCook(string food)
        {
            if (IsFilled)
            {
                return "you are putting to much inside of it";
            }
            if (content.Count == Limit)
            {
                IsFilled = true;
            }
            content.Add(food);
            return "your food was added inside bro";
        }
        public string ListAllTheFoodInside()
        {
            string toReturn = "the food inside the rice cooker are:";
            foreach (string i in content)
            {
                toReturn += "\n" + i;
            }
            return toReturn;
        }
        public string GetTheDish(string dishName)
        {
            string toReturn = "your dish: " + dishName + ", was composed of:";
            foreach (string i in content)
            {
                toReturn += "\n" + i;
            }
            content.Clear();
            return toReturn;
        }
        public string ThrowAtPeople()
        {
            IsBroken = true;
            return "you throw it to people and you pride with it";
        }
        public static void Main(string[] args)
        {

        }
    }
}