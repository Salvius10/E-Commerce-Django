import React, { useState } from "react";
import {useNavigate} from "react-router-dom";
import axios from "axios";
function Register(){
    const [username,setUsername]=useState("")
    const [email,setEmail]=useState("")
    const [password,setPassword]=useState("")
    const navigate=useNavigate();
    const handleSubmit=(e)=>{
        e.preventDefault();
        axios.post("http://localhost:8000/api/account/register/",{
            username:username,
            email:email,
            password:password
        })
        .then(response=>{
            console.log("Registration successfull",response.data);
            navigate("/login");
        })
        .catch(error=>{
            console.error("Registration failed",error.response.data);
        })
    }
    return(
        <form onSubmit={handleSubmit}>
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
            <button type="submit">Register</button>
            
        </form>
    )
}

export default Register;