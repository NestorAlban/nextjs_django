'use client'
import React from "react"

const Home = () => {
    async function buttonCall(){
        try {
          const res = await fetch("http://localhost:8000/polls/courses-views/", {
            method: "POST",
            body: JSON.stringify({
              "course_name": "curso boris",
              "course_description": "curso boris",
              "teacher": "boris"
            }),
            headers: {
              "content-type": "application/json",
            },
          }).catch((e) => console.log(e));
          const data = await res.json();
          console.log(data)
        } catch (err) {
          console.log(err)
        }
        
      } 

    return (

    <button onClick={buttonCall}></button>

        
    )
}

export default Home
