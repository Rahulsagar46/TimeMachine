import React from "react";

const UserCalendar = ({ user, displayDates, weekdaysMap, holidayList, plannedList}) => {
    const checkDateInPlanned = (date) => {
        if(plannedList === undefined){
            return false
        }
        return (plannedList.includes(date) ? true : false)
    }
    return (
            <div className="UserCalendarContainer">
                <div className="UserName">{user}</div>
                <div className="MonthlyCalendarContainer">
                    { 
                        displayDates.map(weekday => { 
                            var date = parseInt(weekday.split("-")[0])
                            var clsName = "CalendarDay CalendarDayCommon"
                            if(checkDateInPlanned(weekday)){
                                clsName = clsName + " " + "CalendarPlanned"
                            } 
                            if(weekdaysMap[weekday][0] === 0 || weekdaysMap[weekday][0] === 6 || holidayList.includes(weekday)){
                                clsName = clsName + " " + "CalendarHoliday"
                            }
                            if(date === 1){
                                clsName = clsName + " " + "CalendarMonthStart"
                            }
                            return (
                                <div className={clsName}>{date}</div>
                                )
                            }
                        )
                    }
                </div> 
            </div>    
        )
}

export default UserCalendar