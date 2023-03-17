import React from "react"
import Courses from "./components/Courses"
import Link from "next/link"

const Home = () => {
    return (
        <main>
            <div>
                <Link href='/courses/create' className="Main-new_course">
                    New Course
                </Link>
            </div>
            <Courses />
        </main>
        
    )
}

export default Home
