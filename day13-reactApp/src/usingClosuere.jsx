import { useState } from "react";

const AppForm = () => {
  const [name, newName] = useState("ok");

  console.log("re-rendered", name);

  // const handleChange = (e) => {
  //   console.log(e.target.value);
    
  //   setTimeout(() => {
  //     newName((prevName) => {
  //       if (e.target.value.length < prevName.length) {
  //         return e.target.value.substring(0, e.target.value.length - 1);
  //       } else {
  //         return e.target.value.toUpperCase();
  //       }
  //     });
  //   }, 0);

  //   newName(e.target.value);
  //   console.log("updated", name);
  // };

  const handleChange = (e) => {
    console.log(e.target.value);
    let val = e.target.value;

    setTimeout(() => {
      newName(val);
    }, 0);
    
    console.log("updated", name);
  };

  return (
    <div>
      <h1>Name</h1>
      <input value={name} type="text" placeholder="Enter here" onChange={handleChange} />
      <p>{name}</p>
    </div>
  );
};

export default AppForm;
