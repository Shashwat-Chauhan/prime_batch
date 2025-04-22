import { useState } from "react"

const AppForm = () => {
  // let name = "Mohan" // React will not manage this variable , because why should it , its sole purpose is to re-render stuff visible on dom , 
  // So for us to make react to manage this variable , we have to use what is called the most basic feature - useState()

  const [name , newName] = useState("ok")
  
  console.log("re-rendered", name)

  const handleChange = (e) => {
    console.log(e.target.value) 

    setTimeout(() => {
      if(e.nativeEvent.inputType === "deleteContentBackward"){
        newName(e.target.value.substring(0, e.target.value.length - 1))
      }
      else{
        newName(e.target.value.toUpperCase() + e.nativeEvent.data) // React says Noted
      }
    },0) // This will give the previous value of mohan , not the currently changed value  

    // This wont work because React will update the name variable after this function completes execution (Single Threaded nature)

    // Like, pure din updates lunga , raat mai saare update krke report krunga , fir kal tumhe saare update dikhenge
    
    newName(e.target.value)
    console.log("updated", name )
  }


  return (
        <div>
            <h1>Name</h1>
            <input value={name} type="text" placeholder="Enter here" onChange={handleChange}/>
            <p>{name}</p>
        </div>
    )
}
export default AppForm