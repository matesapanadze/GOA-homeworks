import React, {useState} from 'react'

export default function Textchange() {
  const [text, setText] = useState("სალამი")
  return (

    <div>
      <h1>{text}</h1>
      <button onClick={() => setText('როგორ ხარ?')}>შეცვალე ტექსტი</button>
    </div>
  )
}
