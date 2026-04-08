using Microsoft.EntityFrameworkCore;

namespace ScriptureApi.Models
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) {}
        public DbSet<Verse> Verses { get; set; }
    }
}