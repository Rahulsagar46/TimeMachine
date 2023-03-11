import React from 'react';
import clsx from 'clsx';
import { DataGrid } from '@mui/x-data-grid';
import getMonthFromIndex from '../../helper';
import {getHoursFromSeconds, getNetWorkingTime} from '../../helper';

const LeftSubcomponent = ({ initialinfo, setInitialinfo }) => {
    const columns = [
        { field: 'col1', headerName: 'Date', width: 95, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col2', headerName: 'Day', width: 95, headerAlign:'center', headerClassName:'DataGridCols' },
        { field: 'col3', headerName: 'Mandatory(hrs) ', width: 100, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col4', headerName: 'Break(hrs) ', width: 80, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col5', headerName: 'Total(hrs)', width: 80, headerAlign:'center', headerClassName:'DataGridCols'},
        { field: 'col6', headerName: 'Net(hrs)', width: 90, headerAlign:'center', type:"string", cellClassName: (params: GridCellParams<string>) =>
        clsx('', {
          NetNegative: params.value.startsWith("-"),
          NetPositive: params.value.startsWith("+"),
        }), headerClassName:'DataGridCols'}
      ];
      const rows = initialinfo["log_entries"] === undefined ? [] : initialinfo["log_entries"].map((row) => ({
          id   : initialinfo["log_entries"].indexOf(row), 
          col1 : row["date"],
          col2 : row["week_day"],
          col3 : getHoursFromSeconds(initialinfo["mandatory_working_time_per_day"]),
          col4 : getHoursFromSeconds(initialinfo["mandatory_break_time"]),
          col5 : getHoursFromSeconds(row["total_work_time_for_day"]),
          col6 : getNetWorkingTime(initialinfo["mandatory_working_time_per_day"], initialinfo["mandatory_break_time"], row["total_work_time_for_day"]) 
      }));
    const dateObj = new Date();
    const currentYear = dateObj.getFullYear();
    const currentMonth = getMonthFromIndex(dateObj.getMonth());
    return (
        <div className='LeftSubcomponent'>
            <div className='LeftSubBanner'>
                <div className="dropdown">
                        <button className="dropbtn">{currentMonth}</button>
                        <div className="dropdown-content">
                            <a href="#">January</a>
                            <a href="#">February</a>
                            <a href="#">March</a>
                            <a href="#">April</a>
                            <a href="#">May</a>
                            <a href="#">June</a>
                            <a href="#">July</a>
                            <a href="#">August</a>
                            <a href="#">September</a>
                            <a href="#">October</a>
                            <a href="#">November</a>
                            <a href="#">December</a>
                        </div>
                </div>
                <div className="dropdown">
                    <button className="dropbtn">{currentYear}</button>
                    <div className="dropdown-content">
                        <a href="#">2023</a>
                        <a href="#">2022</a>
                    </div>
                </div> 
            </div>
            <div className='DataGridContainer'>
                { initialinfo["log_entries"] !== undefined ? <DataGrid rows={rows} columns={columns} rowHeight={30} /> : null }
            </div>
        </div>
    );
}

export default LeftSubcomponent