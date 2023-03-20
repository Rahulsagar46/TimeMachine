import React from 'react';
import axios from 'axios';

const vacationUrl = "http://127.0.0.1:8000/addvacation/"

const VacationForm = ({basicInfo, reloadFunc}) => {
    const vacationAction = (action) => {
        console.log("came here")
        const from = document.getElementById("from").value
        const to = document.getElementById("to").value
        const type = document.getElementById("type").value

        const request = {
                            "common": {
                                        "user": basicInfo["user"],
                                        "vacation_type": type,
                                        "action": action === "plan" ? 0 : 1,
                                        "decision": action === "plan" ? -1 : 0,
                                        "approver": basicInfo["approver"],
                                        "team": basicInfo["team"]
                                    },
                            "actual": [from, to]
                        }
        
        axios.post(vacationUrl, request, {
                            headers: {
                              Accept: 'application/json'
                            }
                          }).then(() => {
                            reloadFunc()
                            }).catch(err => console.log(err));
    }                
    return (
        <div className='VacationFormContainer'>
            <div className='FormWrapper'>
                <div className='FormRow'>
                    <label> From: <input type="date" id='from'/></label>
                    <label> To: <input type="date" id='to'/></label>
                </div>
                <div className='FormRow'  style={{justifyContent: "center"}}>
                    <label>No. of days here</label>
                </div>
                <div className='FormRow' style={{justifyContent: "center"}}>
                    <label>Absence type:</label> 
                    <select style={{marginLeft:"1vmin"}} id='type'>
                        <option value="Urlaub">Urlaub</option>
                        <option value="sick">Krankmeldung</option>
                        <option value="comp">KZE</option>
                    </select>
                </div>
            </div>
            <div className='FormRow' style={{justifyContent: "space-around"}}>
                <button className='ActionButtons' onClick={()=>{vacationAction("plan")}}>Plan</button>
                <button className='ActionButtons' onClick={()=>{vacationAction("apply")}}>Apply</button>
            </div>
        </div>
    )
}

export default VacationForm