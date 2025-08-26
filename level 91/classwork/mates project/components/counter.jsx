import React from 'react'
import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
       <h1>let's count the numbers {count}</h1>
       <button onClick={() => setCount(count + 1)}>click me +</button>
       <button onClick={() => setCount(count - 1)}>click me -</button>
    </div>
  )
}
