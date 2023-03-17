import React from "react";
import { getMaxDaysinMonth } from '../../helper'
import getMonthFromIndex from '../../helper'

const MonthHeader = ({ year, monthIndex, startDate, endDate, maxDaysonCalendar }) => {
    const daysOnDisplay = (endDate - startDate) + 1
    console.log(startDate + " " + endDate)
    console.log(daysOnDisplay)
    const monthDisplay = getMonthFromIndex(monthIndex) + " " + year
    const divWidth = ((daysOnDisplay / maxDaysonCalendar) * 100) + "%" 
    console.log(divWidth + " " + monthDisplay)
    return (
            <div className='MonthHeader' style={{width: divWidth}}>
                {daysOnDisplay >= 7 ? <div>{monthDisplay}</div> : null}
            </div> 
    )
}
export default MonthHeader