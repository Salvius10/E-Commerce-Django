import React, { useState } from "react";
import axios from "axios";
function Login(){
    const [email,setEmail]=useState("");
    const [password,setPassword]=useState("");
    const handleSubmit=(e)=>{
        e.preventDefault();
        axios.post("http://localhost:8000/api/token/",{
            email:email,
            password:password
        })
        .then(response=>{
            console.log("Login success",response.data)
            localStorage.setItem("access",response.data.access);
            localStorage.setItem("refresh",response.data.refresh);
        })
        .catch(error=>{
            console.error("Login Failed",error.response.data)
        });
        console.log("Logeed in with",email,password);
    }
    return(
        <form onSubmit={handleSubmit}>
            <label htmlFor="email">Email: </label>
            <input 
            id="email"
            type="email"
            value={email}
            onChange={(e)=>{setEmail(e.target.value)}}
            placeholder="Enter Email"
             />
             <label htmlFor="pass">Password: </label>
             <input 
             id="pass"
             type="password"
             placeholder="Enter password"
             value={password}
             onChange={(e)=>{setPassword(e.target.value)}}
              />
              <button type="submit">Login</button>
        </form>
    )
}