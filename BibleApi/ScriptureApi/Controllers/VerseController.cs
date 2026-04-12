using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ScriptureApi.Models;

namespace ScriptureApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class VerseController : ControllerBase
    {
        private readonly AppDbContext _context;

        public VerseController(AppDbContext context)
        {
            _context = context;
        }

        // 1. GET: api/Verse (Retrieve All)
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Verse>>> GetVerses()
        {
            return await _context.Verses.ToListAsync();
        }

        // 2. GET: api/Verse/ (Retrieve single)
        [HttpGet("{id}")]
        public async Task<ActionResult<Verse>> GetVerse(int id)
        {
            var verse = await _context.Verses.FindAsync(id);
            if (verse == null) return NotFound();
            return verse;
        }

        // 3. POST: api/Verse (Create)
        [HttpPost]
        public async Task<ActionResult<Verse>> PostVerse(Verse verse)
        {
            _context.Verses.Add(verse);
            await _context.SaveChangesAsync();
            return CreatedAtAction(nameof(GetVerse), new { id = verse.Id }, verse);
        }

        // 4. PUT: api/Verse/ (Update)
        [HttpPut("{id}")]
        public async Task<IActionResult> PutVerse(int id, Verse verse)
        {
            if (id != verse.Id) return BadRequest();

            _context.Entry(verse).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!_context.Verses.Any(e => e.Id == id)) return NotFound();
                throw;
            }
            return NoContent();
        }

        // 5. DELETE: api/Verse/ (Delete)
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteVerse(int id)
        {
            var verse = await _context.Verses.FindAsync(id);
            if (verse == null) return NotFound();

            _context.Verses.Remove(verse);
            await _context.SaveChangesAsync(); // Note: Changed the colon to a semicolon here

            return NoContent();
        }
    }
}
