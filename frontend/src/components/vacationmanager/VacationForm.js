import React from 'react';

const VacationForm = () => {

    return (
        <div className='VacationFormContainer'>
            <form>
                <div className='FormWrapper'>
                    <div className='FormRow'>
                        <label> From: <input type="date"/></label>
                        <label> To: <input type="date"/></label>
                    </div>
                    <div className='FormRow'  style={{justifyContent: "center"}}>
                        <label>No. of days here</label>
                    </div>
                    <div className='FormRow' style={{justifyContent: "center"}}>
                        <label>Absence type:</label> 
                        <select style={{marginLeft:"1vmin"}}>
                            <option value="vacation">Urlaub</option>
                            <option value="sick">Krankmeldung</option>
                            <option value="comp">KZE</option>
                        </select>
                    </div>
                </div>
                <div className='FormRow' style={{justifyContent: "space-around"}}>
                    <button className='ActionButtons'>Plan</button>
                    <button className='ActionButtons'>Apply</button>
                </div>
            </form>
        </div>
    )
}

export default VacationForm