class Human{
    constructor(name, surname, age){
        this.name = name;
        this.surname = surname;
        this.age = age;
    }

    // methods / functions 1
    greeting(){
        console.log(`Hello ${this.name} ${this.surname}`)
    }

    get speak(){
        console.log('hello my friends')
    }

    set someWord(word){
        console.log(word)
    }
}

const newHuman = new Human("mate", "sapanadze", "უბერებელი");


newHuman.greeting()
console.log(newHuman)
