#ifndef FLOCK
#define FLOCK

#include "Boid.hpp"      // Boids
#include "Image.hpp"     // Image (for rendering)
#include "Vec.hpp"       // Vec2D (for COM)
#include <unordered_map> // std::unordered_map
#include <vector>        // std::vector

class Flock
{
  public:
    Flock()
    {
        Params = GlobalParams.FlockParams;
    }
    Flock(const size_t FiD, const size_t Size) : Flock()
    {
        FlockID = FiD;
        for (size_t i = 0; i < Size; i++)
        {
            Boid NewBoid(FlockID);
            Neighbourhood.push_back(NewBoid);
        }
        Valid = (Size > 0);
    }
    size_t FlockID;
    bool Valid;
    Vec2D COM; // center of mass of this flock
    FlockParamsStruct Params;
    std::vector<Boid> Neighbourhood;
    std::unordered_map<size_t, std::vector<size_t>> Buckets; // buckets where the delegates go

    int Size() const;

    void SenseAndPlan(const size_t ThreadID, const std::vector<Flock> &AllFlocks);

    void Act(const double DeltaTime);

    void Delegate(std::vector<Flock> &Flocks);

    void AssignToFlock(std::vector<Flock> &AllFlocks);

    void Recruit(Boid &B, Flock &BsFlock);

    size_t NearestFlockId(const std::vector<Flock> &AllFlocks) const;

    void Draw(Image &I) const;
};

#endif