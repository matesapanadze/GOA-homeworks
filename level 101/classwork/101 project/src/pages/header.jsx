import React from 'react'
import { Link, NavLink } from 'react-router'
export default function Header() {
  const navlink = [{
    title: "Home Create",
    path: "/",
  },
  {
    title: "About",
    path: "/about"
  }]

  return (
    <div>
      {navlink.map((item,index)=>(
        <NavLink to={item.path} key={index}>{item.title}</NavLink>
      ))}
    </div>
  )
}
