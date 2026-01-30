import { useEffect } from "react";
import { useJobsList } from "../../hooks/useJobsList";
import "../../styles/components/list.scss"


function List() {
  const { fetchJobs, result } = useJobsList();

  useEffect(
    () => {
      fetchJobs();
    }, []
  )

  function getTimeZone(date: Date) {
    const offset = date.getTimezoneOffset();
    const hour = Math.trunc(-offset / 60);
    const minutes = -offset % 60;
    if (offset < 0) {
      return `+${hour}:${minutes}`;
    }
    if (offset > 0) {
      return `-${hour}:${minutes}`;
    }
    return "";
  }

  function toLocalDateTime(date: string) {
    const dateTime = new Date(date.replace(" ", "T") + "Z");
    const options: Intl.DateTimeFormatOptions = {
      hour: 'numeric',
      minute: '2-digit',
      hour12: true
    };
    const dateTimeStr = `${dateTime.toLocaleDateString()} ${dateTime.toLocaleTimeString(undefined, options).toLocaleUpperCase()} (GMT${getTimeZone(dateTime)})`;

    return (
      <>
        {dateTimeStr}
      </>
    )
  }

  const generateTable = () => {
    if (result === null) {
      return;
    }

    return result.map((row) => (
      <tr>
        <td><a href={row.url} target="_blank">{row.job_role}</a></td>
        <td>{row.company}</td>
        <td>{toLocalDateTime(row.added_at)}</td>
      </tr>
    ))
  }

  return (
    <table>
      <tr className="title">
        <th>Job Role</th>
        <th>Company</th>
        <th>Added At</th>
      </tr>
      {result && generateTable()}
    </table>
  )
}

export default List;