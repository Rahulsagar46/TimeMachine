import React from 'react';
import {useState} from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { getDaysdelta } from '../../helper';

const AbsenceStatusOverview = ( { plannedList, appliedList} ) => {
    const [activeSideTab, setActiveSideTab] = useState("planned")
    const sortVacationEntries = (targetList) => {
        var targetIds = []
        var targetEntries = {}
        if(targetList === undefined){
            return [targetIds, targetEntries]
        } 
        for(let i = 0; i < targetList.length; i++){
            var entry = targetList[i]
            if(targetIds.includes(entry["vacation_id"])){
                targetEntries[entry["vacation_id"]].push(entry["date"])
            }else{
                targetIds.push(entry["vacation_id"])
                targetEntries[entry["vacation_id"]] = [entry["date"]]
            }
        }
        return [targetIds, targetEntries]
    }
    const [plannedIds, plannedEntries] = sortVacationEntries(plannedList)
    const [appliedIds, appliedEntries] = sortVacationEntries(appliedList)

    const columns = [
        { field: 'col1', headerName: 'From', width: 95, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col2', headerName: 'To', width: 95, headerAlign:'center', headerClassName:'DataGridCols' },
        { field: 'col3', headerName: 'Total', width: 95, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col4', headerName: 'Type', width: 95, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col5', headerName: 'Action', width: 200, headerAlign:'center', headerClassName:'DataGridCols'},
      ];
    const rows = activeSideTab === "planned" ? plannedIds.map((row) => ({
        id   : row, 
        col1 : plannedEntries[row][0],
        col2 : plannedEntries[row][plannedEntries[row].length - 1],
        col3 : getDaysdelta(plannedEntries[row][0], plannedEntries[row][plannedEntries[row].length - 1]),
        col4 : "Urlaub",
        col5 : "Buttons here" 
    })) : appliedIds.map((row) => ({
        id   : row, 
        col1 : appliedEntries[row][0],
        col2 : appliedEntries[row][appliedEntries[row].length - 1],
        col3 : getDaysdelta(appliedEntries[row][0], appliedEntries[row][appliedEntries[row].length - 1]),
        col4 : "Urlaub",
        col5 : "Buttons here" 
    }))
    return (
        <div className='AbsenceStatusOverviewContainer'>
            <div className='SubSideNav'>
                <div className={activeSideTab === "planned" ? 'SubSideNavItem SubSideNavItemActive' : 'SubSideNavItem SubSideNavItemInactive'} onClick={() => {setActiveSideTab("planned")}}> Planned </div>
                <div className={activeSideTab === "applied" ? 'SubSideNavItem SubSideNavItemActive' : 'SubSideNavItem SubSideNavItemInactive'} onClick={() => {setActiveSideTab("applied")}}> Applied </div>
            </div>
            <div className='AbsenceStatusDatagridContainer'>
                <DataGrid checkboxSelection rows={rows} columns={columns} rowHeight={30} />
            </div>
        </div>
    )
}

export default AbsenceStatusOverview