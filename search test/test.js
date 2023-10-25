const nights = 7;  
const startDate = new Date('2024-02-01T00:00:00');  // Assuming the start date is February 1, 2024
const endDate = new Date('2024-02-27T00:00:00');  // Assuming the end date is February 27, 2024
let loopEndDate = new Date(endDate);
loopEndDate.setDate(loopEndDate.getDate() - nights);

// Iterate through each start date within the modified range
for (let d = new Date(startDate); d <= loopEndDate; d.setDate(d.getDate() + 1)) {
  let returnDate = new Date(d);
  console.log("Before:", returnDate);  // Debugging line
  returnDate.setDate(returnDate.getDate() + nights);
  console.log("After:", returnDate);  // Debugging line
  // ... rest of your code
}