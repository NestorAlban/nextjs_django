'use client'
import React, {useContext, useEffect, useState} from 'react';
import Course from './Course';
import '../styles/Courses.css'

const Courses = () => {
  const [courses, setCourses] = useState([]);
  useEffect(() => {
    async function getCoursesGenInfo(){
      try {
        const res = await fetch('http://127.0.0.1:8000/polls/courses-views/')
        const data = await res.json();

        setCourses(data.detail)
        console.log(data)
      } catch (err) {
        console.log(err)
      }
      
    } 
    getCoursesGenInfo()
  }, [])


  return (
    <article className="Courses">
      <div className="Courses-items">
        
        
        {courses.map(course => (
          <Course key={course.id} course={course} />
        ))}
      </div>
    </article>
  );
}

export default Courses;