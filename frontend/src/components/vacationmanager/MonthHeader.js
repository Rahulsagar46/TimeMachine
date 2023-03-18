import React from "react";
import getMonthFromIndex from '../../helper'

const MonthHeader = ({ year, monthIndex, startDate, endDate, maxDaysonCalendar }) => {
    const daysOnDisplay = (endDate - startDate) + 1
    const monthDisplay = getMonthFromIndex(monthIndex) + " " + year
    const divWidth = ((daysOnDisplay / maxDaysonCalendar) * 100) + "%" 
    return (
            <div className='MonthHeader' style={{width: divWidth}}>
                {daysOnDisplay >= 7 ? <div>{monthDisplay}</div> : null}
            </div> 
    )
}
export default MonthHeader