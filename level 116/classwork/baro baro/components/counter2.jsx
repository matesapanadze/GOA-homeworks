import React, { useEffect } from 'react'
import { useState } from 'react'

export default function Counter2() {
    const[count, setCount] = useState(0)
    const [sxva, setSxva] = useState(0)


    useEffect(() => {
        setCount(count + 1)
    }, [sxva])

  return (
    <>
      <div>sxva {sxva}</div>
      <div>count: {count}</div>
      <button onClick={() => setSxva(sxva + 1)}>sxva button</button>
    </>
  )
}
