'use client'
import React, {useContext, useEffect, useState} from 'react';
import Course from '../Course/page';
import '../../styles/Courses.css'

const CreateCourse = () => {
  const [courses, setCourses] = useState([]);
  useEffect(() => {
    async function createNewCourse(){
      try {
        const res = await fetch("http://localhost:3000/polls/courses-views/", {
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

        setCourses(data.detail)
        console.log(data)
      } catch (err) {
        console.log(err)
      }
      
    } 
    createNewCourse()
  }, [])



  return (
    <article className="Courses">
      <div className="Courses-items">
        
        
        <p>Se creó un nuevo curso</p>
      </div>
    </article>
  );
}

export default CreateCourse;