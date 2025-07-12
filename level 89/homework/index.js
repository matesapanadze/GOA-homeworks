class Human{
    constructor(age){
        this.age = age;
    }
    checkAge(){
        if (this.age < 60){
            console.log("this person's age is " + this.age + " years old.\ntherefore this person is young");
        } 
        else {
            console.log("this person's age is " + this.age + " years old.\ntherefore this person is old");
        }        
    }

}

const human = new Human(prompt("enter the age"));
human.checkAge()