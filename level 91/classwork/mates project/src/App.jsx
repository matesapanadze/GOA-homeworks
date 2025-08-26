import React from 'react'
import Mentor from '../components/mentor'
import Assistant from '../components/assistant'
import Students from '../components/students'
import Counter from '../components/counter'
import textchange from '../components/textchange'

export default function App() {
  return (
    <div className='maindiv'>
      <h1>ჯგუფი 48</h1>
      <Mentor />
      <Assistant />
      <Students />
      <Counter />
      <Textchange />
    </div>
  )
}
