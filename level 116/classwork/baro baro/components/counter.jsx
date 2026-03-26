import React from 'react'
import { useState } from 'react'



export default function Counter(){
    const [count, setCount] = useState(0);

    const Increment = () =>{
        setCount(count + 1)
    }
        

    return (
        <div>
            <h1 className='color-black'>let's count {count}</h1>
            <button onClick={Increment()}>+1</button>
        </div>
    )
}

