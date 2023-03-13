import React from "react";

const MonthlyCalendar = ({ user, month, year}) => {
    var rows = []
    for(let i=1; i<=30; i++){
        rows.push(i)
    }
    return (
            <div className="UserNameContainer">
                <div>{user}</div>
                <div className="MonthlyCalendarContainer">
                    { 
                        rows.map(i =>{ return (<div className="CalendarDay">{i}</div>)})
                    }
                </div> 
            </div>    
        )
}

export default MonthlyCalendar