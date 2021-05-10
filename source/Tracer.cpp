#include "Tracer.hpp"
#include <algorithm>
#include <cassert>
#include <iostream>

void Tracer::InitFlockMatrix(const size_t NumFlocks)
{
#ifndef NTRACE
    Tracer *T = Instance();
    for (size_t i = 0; i < NumFlocks; i++)
    {
        // allocate empty dictionary
        T->CommunicationMatrix.push_back(std::vector<FlockOps>(NumFlocks));
    }
    assert(T->CommunicationMatrix.size() * T->CommunicationMatrix[0].size() == sqr(NumFlocks));
#else
    (void)0;
#endif
}

void Tracer::SaveFlockMatrix(const std::vector<Flock> &AllFlocks)
{
#ifndef NTRACE
    Tracer *T = Instance();
    assert(T->CommunicationMatrix.size() > 0);
    for (size_t FID = 0; FID < T->CommunicationMatrix.size(); FID++)
    {
        // for FID being the requestor flock ID
        for (size_t FID2 = 0; FID2 < T->CommunicationMatrix[FID].size(); FID2++)
        {
            // for FID2 being the holder flock ID
            FlockOps &FO = T->CommunicationMatrix[FID][FID2];
            /// NOTE: assigning thread ID's can only be done AFTER all ops have completed
            FO.RequestorTIDs = AllFlocks[FID].TIDs;
            FO.HolderTIDs = AllFlocks[FID2].TIDs;
            Tracer::AddFlockOps(FO);
        }
    }
    // clear matrix
    const size_t NumFlocks = T->CommunicationMatrix.size(); // initial matrix size
    for (auto &Row : T->CommunicationMatrix)
    {
        // reset to all 0's
        Row = std::vector<FlockOps>(NumFlocks);
    }
#else
    (void)0;
#endif
}

void Tracer::AddRead(const size_t F_Requestor, const size_t F_Holder, const Flock::FlockOp F)
{
#ifndef NTRACE
    Tracer *T = Instance();
    assert(T->CommunicationMatrix.size() > 0);
    assert(0 <= F_Requestor && F_Requestor <= T->CommunicationMatrix.size());
    assert(0 <= F_Holder && F_Holder <= T->CommunicationMatrix[0].size());
    switch (F)
    {
    case Flock::SenseAndPlanOp:
#pragma omp atomic
        T->CommunicationMatrix[F_Requestor][F_Holder].SenseAndPlan.Reads++;
    case Flock::DelegateOp:
#pragma omp atomic
        T->CommunicationMatrix[F_Requestor][F_Holder].Delegate.Reads++;
    case Flock::AssignToFlockOp:
#pragma omp atomic
        T->CommunicationMatrix[F_Requestor][F_Holder].AssignToFlock.Reads++;
    }
#else
    (void)0;
#endif
}

void Tracer::AddReads(const size_t T_Requestor, const size_t T_Holder, const size_t Amnt = 1)
{
#ifndef NTRACE
    Tracer *T = Instance();
    assert(T->MemoryOpMatrix.size() == Tracer::Params.NumThreads);
    assert(T->MemoryOpMatrix[0].size() == Tracer::Params.NumThreads);
    assert(0 <= T_Requestor && T_Requestor <= T->MemoryOpMatrix.size());
    assert(0 <= T_Holder && T_Holder <= T->MemoryOpMatrix[0].size());
    T->MemoryOpMatrix[T_Requestor][T_Holder].Reads += Amnt;
#else
    (void)0;
#endif
}

void Tracer::AddFlockOps(const Tracer::FlockOps &FO)
{
#ifndef NTRACE
    // sense & plan
    AddReads(FO.RequestorTIDs.SenseAndPlan, FO.HolderTIDs.SenseAndPlan, FO.SenseAndPlan.Reads);
    // delegate
    AddReads(FO.RequestorTIDs.Delegate, FO.HolderTIDs.Delegate, FO.Delegate.Reads);
    // assign to flock
    AddReads(FO.RequestorTIDs.AssignToFlock, FO.HolderTIDs.AssignToFlock, FO.AssignToFlock.Reads);
#else
    (void)0;
#endif
}

void Tracer::AddTickT(const double ElapsedTime)
{
#ifndef NTRACE
    Tracer *T = Instance();
    T->TickTimes.push_back(ElapsedTime);
#else
    (void)0;
#endif
}

void Tracer::Dump()
{
#ifndef NTRACE
    const Tracer *T = Instance();
    std::cout << "Comms Matrix:" << std::endl;
    for (const std::vector<MemoryOps> &MemoryRow : T->MemoryOpMatrix)
    {
        std::cout << "[ ";
        for (const MemoryOps &M : MemoryRow)
        {
            std::cout << M.Reads << ", ";
        }
        std::cout << "]" << std::endl;
    }
    std::cout << "Tick Timings" << std::endl << "[";
    for (const double t : T->TickTimes)
    {
        std::cout << t << ", ";
    }
    std::cout << "]" << std::endl;
#else
    std::cout << "Trace not executing (compiled with -DNTRACE)" << std::endl;
#endif
}
