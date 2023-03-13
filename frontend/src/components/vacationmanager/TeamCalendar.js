import React from "react";
import MonthlyCalendar from "./MonthlyCalendar";
import { getDateInfo } from "../../helper";

const TeamCalendar = () => {
    const dateInfo = getDateInfo()
    const teamMembers = ["Rahulsagar Voduru", "Fabian Mareyen", "Christoph Juergens"]
    return (
        <div className="TeamCalendarContainer">
            {teamMembers.map(member => {return (<MonthlyCalendar user={member} month={dateInfo.month} year={dateInfo.year}/>)})}
        </div>
            
    )
} 
export default TeamCalendar