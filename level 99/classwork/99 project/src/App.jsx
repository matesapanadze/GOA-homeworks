import React from 'react'
import { BrowserRouter } from "react-router";

export default function App() {

  const navMenuData = [{
    title: "Home",
    path: "/",
  },
  {
    title: "About",
    path: "/about"
  },
  {
    title: "Contacts",
    path: "/contacts"
  },
  {
    title: "Lomi",
    path: "/lomi"
  },
]



  return (
    <div>
      <ul>
        <li>
          <Link to={"/"}>home</Link>
          <Link to={"/about"}>About</Link>
          <Link to={"/contacts"}>Contacts</Link>
          <Link to={"/lomi"}>Lomi</Link>
        </li>
      </ul>
      <header>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contacts" element={<div>Contacts</div>} />
          <Route path="/lomi" element={<div>lomi</div>} />
        </Routes>
      </header>
    </div>
  )
}
