var monthIndexMap = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}

var dayIndexMap = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

export default function getMonthFromIndex(index){
    return monthIndexMap[index];
}

export function getDayFromIndex(index){
    return dayIndexMap[index];
}

export function getDateInfo(dateObjIn=null){
    if(dateObjIn === null){
        var dateObj = new Date()
    }else{
        var dateObj = dateObjIn
    }     
    const returnObj = {
        "dayofmonth" : dateObj.getDate(),
        "month" : dateObj.getMonth(),
        "year" : dateObj.getFullYear(),
        "dateformat1" : String(dateObj.getDate()).padStart(2, 0)+'-'+String(dateObj.getMonth() + 1).padStart(2, 0)+'-'+dateObj.getFullYear(),
        "dateformat2" : dateObj.getFullYear()+'-'+String(dateObj.getMonth() + 1).padStart(2, 0)+'-'+String(dateObj.getDate()).padStart(2, 0),
        "weekdayindex": dateObj.getDay()
    }
    return returnObj;
}

export function getHoursFromSeconds(seconds_in){
    const hours = Math.floor(seconds_in / (60 * 60)) 
    const hours_rem = seconds_in - hours * (60 * 60)  
    const minutes = Math.floor(hours_rem / 60)
    const minute_rem = hours_rem - minutes * 60
    const seconds = minute_rem 
    return (String(hours).padStart(2, 0) + ":" + String(minutes).padStart(2, 0) + ":" + String(seconds).padStart(2, 0));
    // return {"hours": hours, "minutes": minutes, "seconds": seconds};                            
}

export function getElapsedTimeSinceTarget(time){
    const dateObj = new Date()
    const [hoursLast, minutesLast, secondsLast] = time.split(":") 
    const secondsSofar = (parseInt(hoursLast) * 60 * 60) + (parseInt(minutesLast) * 60) + parseInt(secondsLast)
    const secondsCurrent = (dateObj.getHours() * 60 * 60) + (dateObj.getMinutes() * 60) + dateObj.getSeconds()
    const deltaSeconds = secondsCurrent - secondsSofar

    return deltaSeconds;
}

export function getRemainingTime(mandatoryWorkTime, mandatoryBreakTime, elapsedTime){
    const remainingTime = mandatoryWorkTime - elapsedTime
    return remainingTime
}

export function getNetWorkingTime(mandatoryWorkTime, mandatoryBreakTime, actualWorkTime){
    var prefix = "+"
    if(mandatoryWorkTime > actualWorkTime){
        prefix = "-"
    } else if(mandatoryWorkTime === actualWorkTime){
        prefix = ""
    }else{
        prefix = "+"
    }
    const net = getHoursFromSeconds(Math.abs(mandatoryWorkTime - actualWorkTime))
    return (prefix + net)
}

export function getNextWeekDay(currentDayIndex){
    if(currentDayIndex === 6){
        return [0, dayIndexMap[0].slice(0, 2)]
    }
    const nextIndex = currentDayIndex + 1
    return [nextIndex, dayIndexMap[nextIndex].slice(0, 2)]
}

export function getMaxDaysinMonth(year, monthIndex){
    const cat1 = [0, 2, 4, 6, 7, 9, 11] // jan, mar, may, jul, aug, oct, dec
    const cat2 = [3, 5, 8, 10] // apr, jun, sep, nov
    const cat3 = [1] // feb

    if(cat1.includes(monthIndex)){
        return 31
    }else if (cat2.includes(monthIndex)){
        return 30
    }else{
        // TBD add leap year logic here
        return 28
    }
}