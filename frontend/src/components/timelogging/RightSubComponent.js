import React from "react";
import clsx from 'clsx';
import { DataGrid } from '@mui/x-data-grid';
import { getDateInfo, getHoursFromSeconds } from '../../helper';

const RightSubComponent = ({initialinfo}) => {
    const todaysDate = getDateInfo()
    const columns = [
        { field: 'col1', headerName: 'Punch in', width: 85, headerClassName:'DataGridCols' },
        { field: 'col2', headerName: 'Punch out', width: 85, headerClassName:'DataGridCols' },
        { field: 'col3', headerName: 'Duration(hrs)', width: 100, headerClassName:'DataGridCols'},
        { field: 'col4', headerName: 'Status', width: 85, type:'string', cellClassName: (params: GridCellParams<string>) =>
        clsx('', {
          NetNegative: params.value === "unsettled",
          NetPositive: params.value === "settled",
        }), headerClassName:'DataGridCols'}
      ];
    
    const condition1 = initialinfo["log_entries"] !== undefined   
    var condition2 = false
    if (condition1){
        const maxIndex = (initialinfo["log_entries"].length - 1)
        for (var i = maxIndex; i >= 0; i--)
        {
            if(initialinfo["log_entries"][i]["date"] === todaysDate.dateformat2){
                condition2 = true
                var targetIndex = i
                break
            }     
        }
    }
    const rows = (condition1 && condition2) ? initialinfo["log_entries"][targetIndex]["log_entries"].map((row) => ({
        id   : initialinfo["log_entries"][targetIndex]["log_entries"].indexOf(row), 
        col1 : row["log_in_time"],
        col2 : row["log_out_time"],
        col3 : getHoursFromSeconds(row["interval_time"]),
        col4 : row["log_state"] === 0 ? "unsettled" : "settled"
    })) : [];
    return(
        <div className="RightSubComponentContainer">
            <div className="DataGridHeader">{todaysDate.dateformat1}</div>
            <div className="TodaysLog">
                { initialinfo["log_entries"] !== undefined ? <DataGrid rows={rows} columns={columns} rowHeight={30} /> : null }
            </div>
        </div>
    )
}
export default RightSubComponent