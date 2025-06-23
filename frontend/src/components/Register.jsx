import React, { useState } from "react";
function Register(){
    const [username,setUsername]=useState("")
    const [email,setEmail]=useState("")
    const [password,setPassword]=useState("")
    return(
        <form action="">
            <label htmlFor="uname">Enter Username: </label>
            <input 
            id="uname"
            type="text"
            value={username}
            placeholder="Enter username"
            onChange={(e)=>setUsername(e.target.value)} />
            <label htmlFor="email">Enter Email: </label>
            <input 
            id="email"
            type="text"
            value={email}
            placeholder="Enter email"
            onChange={(e)=>setEmail(e.target.value)} />
            <label htmlFor="pass">Enter Password: </label>
            <input type="text"
            id="pass"
            value={password}
            placeholder="Enter Password"
            onChange={(e)=>setPassword(e.target.value)} />
            <button>Register</button>
            
        </form>
    )
}

export default Register;