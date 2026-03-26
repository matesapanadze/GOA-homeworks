import { useState } from 'react';
import "./App.css";

interface AcademyInterface {
    email: {
        _id: string;
        points: number;
        rating: number
    }
}







interface UserInterface extends AcademyInterface {
    name: string;
    age: number;
}



export default function App() {
    const [user, setUser] = useState<UserInterface>();
  return (
    <div>
      
    </div>
  )
}
