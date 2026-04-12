using Microsoft.EntityFrameworkCore;
using ScriptureApi.Models;


var builder = WebApplication.CreateBuilder(args);

// 1. Add controller support
builder.Services.AddControllers();

// 2. Setup the In-Memory Database
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseInMemoryDatabase("BibleDb"));


// 3. Add Swagger generation services
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// 4. Configure the HTTP request pipeline
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

// 5. Map the controllers 
app.MapControllers();

app.Run();
    
