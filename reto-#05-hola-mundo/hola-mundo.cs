class helloWorld
{
    public static void main(String[] args) {
        System.out.println("Hello World!");
        int a = 10; // declaration and initialization of variable 'a'
        if (true){
            String s = "hello";//declaration and initialization of string object in the block scope
            for (int i=2 ;i<=5;++i)//for loop with increment operator
            System.out.print(s+" "+++a);
            }
            else {//else statement
            while (--a>4);//while loop with decrement operator
            System.out.printf("%d ",++a);
            do
            {
                ++a;//do-while loop with prefix increment operator
            }while (++a<6);
        }
    }
}