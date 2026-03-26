import React from "react";

import MyRouter from "./components/router";

import "./App.css";

import { useEffect, useState } from "react";
export default function App() {

    const [data, setData] = useState([]);

    useEffect(() => {

    async function fetchData() {

    const URL = "https://jsonplaceholder.typicode.com/users";

    const response = await fetch(URL);

    const data = await response.json();

    setData(data);
    }
  }
}     