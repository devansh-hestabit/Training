export default function DataTable() {
  const data = [
    {
      name: "Liam O'Connell",
      position: "Cloud Infrastructure Lead",
      office: "Dublin",
      age: 38,
      startDate: "2016/09/14",
      salary: "$142,500",
    },
    {
      name: "Aiko Tanaka",
      position: "Senior Financial Analyst",
      office: "Osaka",
      age: 41,
      startDate: "2018/02/05",
      salary: "$118,200",
    },
    {
      name: "María González",
      position: "Technical Documentation Specialist",
      office: "Madrid",
      age: 34,
      startDate: "2020/06/21",
      salary: "$72,450",
    },
    {
      name: "Ethan Brooks",
      position: "Frontend Performance Engineer",
      office: "Austin",
      age: 29,
      startDate: "2021/11/03",
      salary: "$131,900",
    },
  ];

  return (
    <table className="w-full text-sm text-left border-collapse">
      <thead>
        <tr className="bg-gray-50 border-b">
          <th className="px-3 py-2 font-medium-semibold text-black">Name</th>
          <th className="px-3 py-2 font-medium-semibold text-black">
            Position
          </th>
          <th className="px-3 py-2 font-medium-semibold text-black">Office</th>
          <th className="px-3 py-2 font-medium-semibold text-black">Age</th>
          <th className="px-3 py-2 font-medium-semibold text-black">
            Start date
          </th>
          <th className="px-3 py-2 font-medium-semibold text-black">Salary</th>
        </tr>
      </thead>

      <tbody>
        {data.map((row, index) => (
          <tr
            key={index}
            className={`border-b ${
              index % 2 === 0 ? "bg-white" : "bg-gray-50"
            }`}
          >
            <td className="px-3 py-2 text-gray-700">{row.name}</td>
            <td className="px-3 py-2 text-gray-700">{row.position}</td>
            <td className="px-3 py-2 text-gray-700">{row.office}</td>
            <td className="px-3 py-2 text-gray-700">{row.age}</td>
            <td className="px-3 py-2 text-gray-700">{row.startDate}</td>
            <td className="px-3 py-2 text-gray-700 ">{row.salary}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
