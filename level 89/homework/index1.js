class Humans {
    constructor() {
        this.people = [];
    }

    addPerson(name, age) {
        this.people.push({ name, age });
    }

    showOlderThan50() {
        const olderPeople = this.people.filter(person => person.age > 50);
        
        console.log("50 წელს გადაცილებული ადამიანები:");
        olderPeople.forEach(person => {
            console.log(`${person.name} არის ${person.age} წლის`);
        });
    }
}

// გამოყენება:
const group = new Humans();

group.addPerson("გიორგი", 45);
group.addPerson("მარიამი", 52);
group.addPerson("დავითი", 61);
group.addPerson("ნინა", 30);

group.showOlderThan50();