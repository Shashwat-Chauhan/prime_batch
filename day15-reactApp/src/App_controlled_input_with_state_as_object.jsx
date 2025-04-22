import React, { useState } from 'react'
import p from "papaparse"
import Card from './Card'

const App_controlled_input_with_state_as_object = () => {
    const [profiles , setProfiles] = useState([])
    const handleFileUpload = (e) => {
        const file = e.target.files[0]
        p.parse(file , {header: true, complete : handleData})
    }

    const handleData = (res) => {
        const {data , errors} = res
        if (errors.length > 0){
            alert("Error")
        }
        else{
            setProfiles(data)
            console.log(data)
        }
    }
  return (
    <div>
      <div>
        <input type="file" accept='.csv' onChange={handleFileUpload} />
      </div>
      <div>
        {profiles.map((elem , index) => {
            return <Card
                key = {index}
                name= {elem.name}
                email = {elem.email}
                githubLink = {elem.githubLink}
            />
        })}
        
      </div>
    </div>
  )
}


export default App_controlled_input_with_state_as_object
