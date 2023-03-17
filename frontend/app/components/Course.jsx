import React from 'react';
import dia_image1 from '../images/dia_image1.png'
import Dia1 from './placeim/diaiam.png'
import '../styles/Course.css'




const Course = ({ course}) => {
  const date_format = course.creation
  const date_day = date_format.slice(0,10).split('-').join('/')
  const date_time = date_format.slice(11,19)
  return (
    <div className="Course-item">
      <div className='Course-item_card'>
        <div className='Course-item_img'>
          <img key={course.id} src={Dia1.src} alt={course.name} />
        </div>
        
        <div className="Course-item-info">
          <div className='Course-item-info_main'>
            <p>{course.name}</p>
            
            <p>{course.teacher}</p>
          </div>
          <div className='Course-item-info_extra'>
            <p>{course.description}</p>
            <p>{course.reviews}</p>
          </div>
          <p>{date_day} at {date_time}</p>
        </div>
      </div>
      
    </div>
  );
}

export default Course;