import React from "react";

const UserCalendar = ({ user, displayDates, weekdaysMap}) => {
    
    return (
            <div className="UserCalendarContainer">
                <div className="UserName">{user}</div>
                <div className="MonthlyCalendarContainer">
                    { 
                        displayDates.map(weekday => { 
                            var clsName = "CalendarDay CalendarDayCommon"
                            if(weekdaysMap[weekday][0] === 5 || weekdaysMap[weekday][0] === 6){
                                clsName = clsName + " " + "CalendarHoliday"
                            }
                            if(weekday==31){
                                clsName = clsName + " " + "CalendarMonthEnd"
                            }
                            return (
                                <div className={clsName}>{weekday}</div>
                                )
                            }
                        )
                    }
                </div> 
            </div>    
        )
}

export default UserCalendar